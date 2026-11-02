from buildchecker.fullcheck import project_path

def test_student_path_normalization():
    assert project_path("./src/../config.h", "/course/project", "/course/project") == "config.h"
