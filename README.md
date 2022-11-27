# secret-santa

Lets you do Secret Santa assignments by providing the program with `people` and
`households`.  Participants will be  emailed their randomly assigned giftee.
Participants cannot be assigned someone from their own household.

## Prerequisites

* [python3.10+](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/)

### Ubuntu

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
curl -sSL https://install.python-poetry.org | python3.10 -
```

-----

## Bootstrap Repository

```bash
git clone git@gitlab.com:adveres/leetcode.git
cd leetcode
poetry install
poetry shell
```

-----

## Usage

```bash
python3 secret_santa.py --help
```

1. Edit [santa_common/houses.py](santa_common/houses.py) and add some households.
2. Edit [santa_common/people.py](santa_common/people.py) and add some people.
3. Run the program, supplying required arguments.
    * *By default it's just a dry-run of the pairings instead of actually sending emails.*
4. Input your email password, when prompted, if `--send-emails` param was given

-----
-----

## Points of Improvement

* Only works with gmail (could add SMTP param)
* Have to handcraft JSON files with people + addresses. Yuck. (read from gDrive? gContacts?)
* I'd like to preview the emails without having to send them (write HTML file)
* Better to template email text/HTML instead of what I'm doing (jinja?)
* Algorithm for selecting giftee is random and may fail (it retries if it fails)
* Hardcoded email subject
* Tests
* Rules for assigning are hardcoded. For example if only one house wants to play it won't work.
