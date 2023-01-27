from pathlib import Path
from dovado_rtl.parsers.vhdl.vhdl_parsed import VhdlParsed
from dovado_rtl.parsers.vhdl.vhdl_parser import VhdlParser
import os


def test_neorv_top_parsing():
    path_prexif: str = "../" + os.curdir + "/resources"
    to_parse = Path(path_prexif + "/neorv32/rtl/core/neorv32_top.vhd")
    parser = VhdlParser()
    parsed: VhdlParsed = parser.parse(Path(to_parse))

    # Only scalar parameters are supported
    assert len(parsed.entities) == 1
    entity = parsed.entities[0]

    assert len(entity.parameters) == 69
    assert len(entity.ports) == 58

    non_default_parameter = entity.parameters[0]
    default_parameter = entity.parameters[1]

    assert non_default_parameter.name == "CLOCK_FREQUENCY"
    assert non_default_parameter.value == ""
    assert non_default_parameter.rule.getText() == "natural"

    assert default_parameter.name == "HW_THREAD_ID"
    assert default_parameter.value == "0"
    assert default_parameter.rule.getText() == "0"

    clk_port = entity.ports[0]

    assert clk_port.name == "clk_i"

    assert (
        parsed.replace({"CLOCK_FREQUENCY": "10", "HW_THREAD_ID": "11"})
        == Path(path_prexif + "/replaced_neorv_top.vhd").read_text()
    )
