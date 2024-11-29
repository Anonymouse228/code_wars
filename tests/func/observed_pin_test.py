import pytest

from observed_pin import get_pins, get_pins2


def test_answers():
    data = {
        '0': ['8', '0'],
        '8': ['5', '7', '8', '9', '0'],
        '11': ["11", "22", "44", "12", "21", "14", "41", "24", "42"],
        '369': ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
                "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
                "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"],
        '9578': ['9578', '9575', '9577', '9579', '9570', '9548', '9545', '9547', '9549', '9540', '9588', '9585', '9587',
                 '9589', '9580', '9278', '9275', '9277', '9279', '9270', '9248', '9245', '9247', '9249', '9240', '9288',
                 '9285', '9287', '9289', '9280', '9478', '9475', '9477', '9479', '9470', '9448', '9445', '9447', '9449',
                 '9440', '9488', '9485', '9487', '9489', '9480', '9678', '9675', '9677', '9679', '9670', '9648', '9645',
                 '9647', '9649', '9640', '9688', '9685', '9687', '9689', '9680', '9878', '9875', '9877', '9879', '9870',
                 '9848', '9845', '9847', '9849', '9840', '9888', '9885', '9887', '9889', '9880', '6578', '6575', '6577',
                 '6579', '6570', '6548', '6545', '6547', '6549', '6540', '6588', '6585', '6587', '6589', '6580', '6278',
                 '6275', '6277', '6279', '6270', '6248', '6245', '6247', '6249', '6240', '6288', '6285', '6287', '6289',
                 '6280', '6478', '6475', '6477', '6479', '6470', '6448', '6445', '6447', '6449', '6440', '6488', '6485',
                 '6487', '6489', '6480', '6678', '6675', '6677', '6679', '6670', '6648', '6645', '6647', '6649', '6640',
                 '6688', '6685', '6687', '6689', '6680', '6878', '6875', '6877', '6879', '6870', '6848', '6845', '6847',
                 '6849', '6840', '6888', '6885', '6887', '6889', '6880', '8578', '8575', '8577', '8579', '8570', '8548',
                 '8545', '8547', '8549', '8540', '8588', '8585', '8587', '8589', '8580', '8278', '8275', '8277', '8279',
                 '8270', '8248', '8245', '8247', '8249', '8240', '8288', '8285', '8287', '8289', '8280', '8478', '8475',
                 '8477', '8479', '8470', '8448', '8445', '8447', '8449', '8440', '8488', '8485', '8487', '8489', '8480',
                 '8678', '8675', '8677', '8679', '8670', '8648', '8645', '8647', '8649', '8640', '8688', '8685', '8687',
                 '8689', '8680', '8878', '8875', '8877', '8879', '8870', '8848', '8845', '8847', '8849', '8840', '8888',
                 '8885', '8887', '8889', '8880']
    }
    functions = (get_pins, get_pins2)

    for function in functions:
        print(function.__name__)
        for key, value in data.items():
            assert sorted(function(key)) == sorted(value)


def test_input():
    with pytest.raises(TypeError) as info:
        get_pins(1234)

    info = info.value.args[0]
    assert info == '\'int\' object is not iterable'
