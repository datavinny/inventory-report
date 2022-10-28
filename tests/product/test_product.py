from inventory_report.inventory.product import Product

ID = 1
PRODUCT_NAME = "gel plumaluz"
OWNER = "Zalie Moda Expedicionária & Miudezas"
FABRICATION_DATE = "21/12/2002"
EXPIRATION_DATE = "21/01/2003"
SERIE_NUMBER = 21012
INSTRUCTIONS = "instructions"

mock_res = "<bound method Product.__repr__ of O produto gel plumaluz fabricado\
 em 21/12/2002 por Zalie Moda Expedicionária & Miudezas com\
 validade até 21/01/2003 precisa ser armazenado instructions.>"


def test_cria_produto():
    test_product = Product(
      ID,
      PRODUCT_NAME,
      OWNER,
      FABRICATION_DATE,
      EXPIRATION_DATE,
      SERIE_NUMBER,
      INSTRUCTIONS)
    assert str(test_product.__repr__) == mock_res
