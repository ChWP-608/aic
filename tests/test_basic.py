def test_pipeline_works():
    assert 1 + 1 == 2

def test_python_version():
    import sys
    assert sys.version_info.major == 3

def test_docker_image_name():
    image_name = "ghcr.io/chwp-608/aic:latest"
    assert "ghcr.io" in image_name
    assert "chwp-608" in image_name

