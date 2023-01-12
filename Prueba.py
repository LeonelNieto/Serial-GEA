from crc import Calculator, Configuration

config = Configuration(
    width=8,
    poly=0x07,
    init_value=0x00,
    final_xor_value=0x00,
    reverse_input=False,
    reverse_output=False,
)

calculator = Calculator(config)