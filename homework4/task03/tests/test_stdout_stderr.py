from homework4.task03.stdout_stderr import my_precious_logger


def test_stdout_stderr_function_example1(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert err == "error: file not found\n"
    assert out == ""


def test_stdout_stderr_function_example2(capsys):
    my_precious_logger("ok")
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "ok\n"


def test_stdout_stderr_function_example3(capsys):
    my_precious_logger("")
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "\n"


def test_stdout_stderr_function_example4(capsys):
    my_precious_logger("1234567")
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "1234567\n"
