from myproj.text import slugify


def test_slugify_basic():
    assert slugify("Hello, world!") == "hello-world"
