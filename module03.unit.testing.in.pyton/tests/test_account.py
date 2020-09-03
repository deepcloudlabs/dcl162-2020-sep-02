import pytest

from banking.domain import Account, InsufficientBalance


@pytest.fixture
def an_account():
    return Account("tr1", 1000)


def test_create_account(an_account):
    assert an_account.iban == "tr1"
    assert an_account.balance == 1000


def test_deposit_with_positive_amount_then_success(an_account):
    an_account.deposit(1)
    assert an_account.balance == 1001


def test_deposit_with_negative_amount_then_fails(an_account):
    with pytest.raises(ValueError):
        an_account.deposit(-1)
    assert an_account.balance == 1000


def test_withdraw_all_balance_then_success(an_account):
    an_account.withdraw(1000)
    assert an_account.balance == 0


def test_withdraw_over_balance_then_fails(an_account):
    with pytest.raises(InsufficientBalance) as e:
        an_account.withdraw(1001)
        assert e.deficit == 1
    assert an_account.balance == 1000


def test_withdraw_with_negative_amount_then_fails(an_account):
    with pytest.raises(ValueError):
        an_account.withdraw(-1)
    assert an_account.balance == 1000
