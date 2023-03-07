from pytest_mock import MockerFixture
def test_app(mocker: MockerFixture):
    import app
    res_main = app.main()
    assert res_main == 100 or res_main == 400


def test_app_testable(mocker: MockerFixture):
    from app import main2_testable
    import app
    spy_multiplication = mocker.spy(app, 'multiplication')
    spy_square = mocker.spy(app, 'square')
    assert main2_testable() == 400
    # spy_multiplication.assert_called_once
    spy_multiplication.assert_called_once_with(10, 2)
    assert spy_multiplication.spy_return == 20
    