from __future__ import annotations

import os
import traceback
from typing import TYPE_CHECKING

import pytest

from example_app.features.runtime_configuration.adapters.inbound.env_settings_adapter import (
    EnvSettingsAdapter,
)
from example_app.features.runtime_configuration.adapters.inbound.env_settings_adapter.settings import (
    EnvSettings,
    OUTPUT_PATH_ALIAS,
    REQUIRED_SECRET_ALIAS,
    SERVICE_URL_ALIAS,
)
from example_app.features.runtime_configuration.application.dtos.app_settings import (
    DEFAULT_OUTPUT_PATH,
    DEFAULT_SERVICE_URL,
)
from example_app.features.runtime_configuration.application.exceptions import ConfigurationError

if TYPE_CHECKING:
    from pathlib import Path

REQUIRED_SECRET_VALUE = 'local-secret-value'


@pytest.fixture(autouse=True)
def isolate_env_file_lookup(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Prevent developer-local `.env` files from affecting settings tests."""
    monkeypatch.chdir(tmp_path)
    names = {
        REQUIRED_SECRET_ALIAS.casefold(),
        SERVICE_URL_ALIAS.casefold(),
        OUTPUT_PATH_ALIAS.casefold(),
        'required_secret',
        'service_url',
        'output_path',
    }
    for name in tuple(os.environ):
        if name.casefold() in names:
            monkeypatch.delenv(name)


def test_missing_required_secret_raises_configuration_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(REQUIRED_SECRET_ALIAS, raising=False)
    monkeypatch.delenv(OUTPUT_PATH_ALIAS, raising=False)

    with pytest.raises(ConfigurationError, match='Invalid runtime configuration'):
        EnvSettingsAdapter().load()


def test_invalid_configuration_traceback_does_not_expose_input(tmp_path: Path) -> None:
    sensitive_value = 'test-secret-42'
    (tmp_path / '.env').write_text(f'UNRELATED_SECRET={sensitive_value}\n', encoding='utf-8')

    with pytest.raises(ConfigurationError) as exc_info:
        EnvSettingsAdapter().load()

    rendered = ''.join(traceback.format_exception(exc_info.value))
    assert sensitive_value not in rendered
    assert 'ValidationError' not in rendered
    assert 'Invalid runtime configuration' in rendered


@pytest.mark.parametrize('raw_value', ['', '   '])
def test_blank_required_secret_raises_configuration_error(monkeypatch: pytest.MonkeyPatch, raw_value: str) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, raw_value)

    with pytest.raises(ConfigurationError, match='Invalid runtime configuration'):
        EnvSettingsAdapter().load()


def test_valid_required_secret_loads_app_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, f"  {REQUIRED_SECRET_VALUE}  ")
    monkeypatch.delenv(SERVICE_URL_ALIAS, raising=False)
    monkeypatch.delenv(OUTPUT_PATH_ALIAS, raising=False)

    settings = EnvSettingsAdapter().load()

    assert settings.required_secret == REQUIRED_SECRET_VALUE
    assert settings.service_url == DEFAULT_SERVICE_URL
    assert settings.output_path == DEFAULT_OUTPUT_PATH


def test_service_url_override_loads_app_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)
    monkeypatch.setenv(SERVICE_URL_ALIAS, '  https://service.example.test  ')

    settings = EnvSettingsAdapter().load()

    assert settings.service_url == 'https://service.example.test'


def test_blank_service_url_raises_configuration_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)
    monkeypatch.setenv(SERVICE_URL_ALIAS, '  ')

    with pytest.raises(ConfigurationError, match='Invalid runtime configuration'):
        EnvSettingsAdapter().load()


def test_output_path_override_loads_app_settings(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    output_path = tmp_path / 'output.sqlite3'
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)
    monkeypatch.setenv(OUTPUT_PATH_ALIAS, f"  {output_path}  ")

    settings = EnvSettingsAdapter().load()

    assert settings.output_path == output_path


def test_blank_output_path_raises_configuration_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)
    monkeypatch.setenv(OUTPUT_PATH_ALIAS, '  ')

    with pytest.raises(ConfigurationError, match='Invalid runtime configuration'):
        EnvSettingsAdapter().load()


def test_unrelated_environment_variables_are_ignored(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)
    monkeypatch.setenv('UNRELATED_SETTING', 'ignored')

    settings = EnvSettingsAdapter().load()

    assert settings.required_secret == REQUIRED_SECRET_VALUE


def test_environment_overrides_dotenv(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    (tmp_path / '.env').write_text(
        f'{REQUIRED_SECRET_ALIAS}=file-secret\n{SERVICE_URL_ALIAS}=https://file.example.test\n',
        encoding='utf-8',
    )
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)
    monkeypatch.setenv(SERVICE_URL_ALIAS, 'https://environment.example.test')

    settings = EnvSettingsAdapter().load()

    assert settings.required_secret == REQUIRED_SECRET_VALUE
    assert settings.service_url == 'https://environment.example.test'


def test_blank_environment_does_not_fall_back_to_dotenv(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    (tmp_path / '.env').write_text(f'{REQUIRED_SECRET_ALIAS}=file-secret\n', encoding='utf-8')
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, '')

    with pytest.raises(ConfigurationError, match='Invalid runtime configuration'):
        EnvSettingsAdapter().load()


def test_settings_repr_does_not_expose_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)

    assert REQUIRED_SECRET_VALUE not in repr(EnvSettingsAdapter().load())


def test_adapter_model_repr_does_not_expose_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(REQUIRED_SECRET_ALIAS, REQUIRED_SECRET_VALUE)

    assert REQUIRED_SECRET_VALUE not in repr(EnvSettings())  # type: ignore[call-arg]


def test_dotenv_loads_without_environment_values(tmp_path: Path) -> None:
    (tmp_path / '.env').write_text(f'{REQUIRED_SECRET_ALIAS}=file-secret\n', encoding='utf-8')

    settings = EnvSettingsAdapter().load()

    assert settings.required_secret == 'file-secret'
    assert settings.service_url == DEFAULT_SERVICE_URL
    assert settings.output_path == DEFAULT_OUTPUT_PATH


def test_case_insensitive_field_name_inputs_load(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv('ReQuIrEd_SeCrEt', REQUIRED_SECRET_VALUE)

    assert EnvSettingsAdapter().load().required_secret == REQUIRED_SECRET_VALUE
