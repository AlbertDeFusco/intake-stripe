from intake-stripe import cli

def test_cli_template():
    assert cli.cli() is None
