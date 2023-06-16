from utils.dicts import get_val


def test_get_val(data):
    assert get_val(data[0], "vcs") == "mercurial"
    assert get_val(data[0], "rty") == "git"
    assert get_val(data[1], "vcs", "jkl") == "jkl"
