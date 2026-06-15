from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]


def test_pyproject_configures_uv_and_setuptools_build():
    pyproject = tomllib.loads((ROOT / 'pyproject.toml').read_text())

    assert pyproject['project']['name'] == 'pydu'
    assert pyproject['build-system']['build-backend'] == 'setuptools.build_meta'
    assert 'dev' in pyproject['dependency-groups']


def test_makefile_uses_uv_for_common_development_tasks():
    makefile = (ROOT / 'Makefile').read_text()

    assert 'uv sync' in makefile
    assert 'uv run' in makefile
    assert 'uv build' in makefile
    assert 'uv publish' in makefile


def test_release_workflow_builds_github_release_and_publishes_with_uv():
    workflow = (ROOT / '.github' / 'workflows' / 'release.yml').read_text()

    assert 'v*.*.*' in workflow
    assert 'uv build' in workflow
    assert 'softprops/action-gh-release' in workflow
    assert 'UV_PUBLISH_TOKEN: ${{ secrets.PYPI_TOKEN }}' in workflow
    assert 'uv publish' in workflow


def test_github_workflows_use_current_setup_uv_action():
    workflows = [
        ROOT / '.github' / 'workflows' / 'release.yml',
        ROOT / '.github' / 'workflows' / 'test.yml',
    ]

    for workflow in workflows:
        assert 'astral-sh/setup-uv@v8' in workflow.read_text()
