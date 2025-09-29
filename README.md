# wikibot.py Wikipedia Bot for Mastodon

This is a simple bot for mastodon, which posts the content of Wikipedia's "on this day" feed during the day.

Follow it at https://chaos.social/@Wikibot (It currently only speaks German)

Bug reports and feature requests welcome!

## Installation

Wikibot uses [uv](https://docs.astral.sh/uv/) as package manager, so make sure it is installed.

To access Mastodon you must generate an access token in Mastodon and place it in a `.env` file at the root of this repo like so: `MASTODON_ACCESS_TOKEN=<your_token>`

You can then run the bot using `uv run python wikibot.py`. Use `--dry-run` to see the output on the command line instead of creating a post.

It is recommended to run the bot as a [systemd timer](https://wiki.archlinux.org/title/Systemd/Timers). Templates for the 
timer itself and the service it invokes can be found in `systemd`.

You can automatically render the template and install and start the timer using `uv run python install.py`.