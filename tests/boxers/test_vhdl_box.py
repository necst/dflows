from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from dovado_rtl.parsers.vhdl.parse import parse
from dovado_rtl.boxers.vhdl.boxer import VhdlBoxer
from pathlib import Path
from typing import cast


def test_vhdl_box():

    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(Path("resources/configs/test_config.toml"))
    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)
    boxer = VhdlBoxer()
    boxer.box(design_point)
    assert (
        Path("dovado_work/box.vhd").read_text()
        == Path("resources/neorv_box.vhd").read_text()
    )

    assert boxer.boxed
