from scripts.aave_borrow import (
    get_asset_price,
    get_lending_pool,
    approve_erc20,
    get_account,
)
from brownie import network, config


def test_get_asset_price():
    # Arrange / Act
    asset_price = get_asset_price(
        config["networks"][network.show_active()]["dai_eth_price_feed"]
    )
    assert asset_price > 0.0, "Failed"


def test_get_borrowale_data():
    pass


def test_get_lending_pool():
    lending_pool = get_lending_pool()
    assert lending_pool is not None, "Failed"


def test_approve_erc20():
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 1000000000000000000  # 1
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    assert tx is not None, "Failed"
