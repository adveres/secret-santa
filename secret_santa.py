"""
A secret santa script to email people their recipients.
"""
import argparse
import logging
import smtplib
import ssl
import getpass

from prettytable import PrettyTable

from santa_common import email, matchmaker
from santa_common.people import EVERYONE

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s [%(module)-12s] - %(message)s",
)


def _pprint_pairs(pairs):
    my_table = PrettyTable()

    my_table.field_names = ["Giver", "Receiver"]
    for my_pair in pairs:
        giver, receiver = my_pair

        emailed = [giver.email]
        if giver.cc is not None:
            emailed.extend(giver.cc)

        emailed = ",".join(emailed)
        my_table.add_row([f"{giver} <{emailed}>", receiver])

    print(my_table)


def send_email_from_pairs(pairs, sender_email):
    password = getpass.getpass(
        f"Type email password for '{sender_email}' and press enter:"
    )

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        logging.debug("Logging in as %s", sender_email)
        server.login(sender_email, password)

        for my_pair in sorted(pairs, key=lambda x: x[0].household.address_1):
            giver, receiver = my_pair
            logging.info(
                f"{giver.first} {giver.last} -> {receiver}. Emailing <{giver.email}>"
            )
            message = email.make_mime_message(sender_email, giver, receiver)
            server.sendmail(sender_email, giver.email, message.as_string())


def main(send_emails, sender_email):
    # TODO smarter way of getting people data than hardcoded objects
    if not EVERYONE:
        logging.error(
            "EVERYONE tuple from 'common.people' module is empty. Populate it."
        )
        return 1

    pairs = matchmaker.make_pairs(EVERYONE)
    _pprint_pairs(pairs)

    if send_emails:
        logging.debug("Sending emails as <%s>", sender_email)
        send_email_from_pairs(pairs, sender_email)
    else:
        logging.info("No emails were actually sent!")

    return 0


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(
        description="Assigns people random 'Secret Santa' giftees. By default the program doesn't actually send the "
        "emails to prevent accidents. There's an arg for that!",
        epilog="Merry Christmas!",
    )
    my_parser.add_argument(
        "-e",
        "--sender-email",
        required=True,
        help="What email to use as the sender for the emails.",
    )
    my_parser.add_argument(
        "--send-emails",
        action="store_true",
        help="Actually sends the emails instead of outputting the dry-run of what would happen.",
    )

    args = my_parser.parse_args()

    ret = main(args.send_emails, args.sender_email)
    exit(ret)
