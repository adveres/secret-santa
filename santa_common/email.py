"""
Helps create email messages
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .people import Person


def make_mime_message(sender_email: str, giver: Person, receiver: Person) -> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["Subject"] = f"🎅 Pst {giver.first}, your 2020 Secret Santa pick is here! 🎅"
    message["From"] = sender_email
    message["To"] = giver.email

    # Optional CC of giver (if a kid needs to also give a gift but doesn't shop)
    if giver.cc is not None:
        message["CC"] = ",".join(giver.cc)  # Seems to work for multiple emails or single ones.

    # Create the plain-text and HTML version of your message
    text = f"""
    Hi, {giver.first}!

    You've been assigned {receiver.first} as your secret-Santa recipient.
    Their full address is: 

    {receiver.first} ${receiver.last}
    {receiver.household.address_1}
    {receiver.household.address_2}
    
    Remember the price limit is $30!
    We can start a big email thread with peoples' wish lists separately.
    This is secret, don't spill who was assigned to you! 🙊
    Double check shipping information before you send your gift.

    Merry Christmas!
    """
    if receiver.household.notes is not None:
        text += "\n\n" + receiver.household.notes

    html = f"""\
    <html>
      <body>
        <p>Hi, <b>{giver.first}</b>!<br><br>
        <h2>🎁 Who? 🎁</h2>
        You've been assigned <b>{receiver.first}</b> ({receiver.email}) as your Secret Santa recipient. 
        Their full address is: <br>
        <blockquote>
        <b>{receiver.first} {receiver.last}</b><br>
        <b>{receiver.household.address_1}</b><br>
        <b>{receiver.household.address_2}</b><br>
        </blockquote>
        <h2>🎁 Details 🎁</h2>
        <ul>
        <li>The price limit is $30</li>
        <li>We can start a big email thread with peoples' wish lists separately</li>
        <li>This is secret, don't spill who was assigned to you! 🙊</li>
        <li>Double check shipping information before you send your gift.</li>
    """
    if receiver.household.notes is not None:
        html += "<li><b><u>Special notes for this address:</u></b> " + receiver.household.notes + "</li>"
    html += "</ul><br>🎄 Merry Christmas! 🎄</p></body></html>"

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    return message
