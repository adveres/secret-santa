from santa_common.email import make_email_content

from santa_common.people import Person


def test_make_email_content(person_simple: Person, person_parent: Person, snapshot):
    res = make_email_content(person_simple, person_parent)

    print(res["plain"])
    print(res["html"])

    assert res == snapshot

    # Convenient to see the HTML in-browser sometimes
    #
    # with open("zz_test_output.html", "w") as my_file:
    #     my_file.write(res["html"])
