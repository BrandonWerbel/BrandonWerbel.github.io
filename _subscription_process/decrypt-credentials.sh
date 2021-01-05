#!/bin/sh

# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$CREDENTIALS_PASSPHRASE" \
--output _subscription_process/credentials.json _subscription_process/encrypted-credentials.json.gpg

gpg --quiet --batch --yes --decrypt --passphrase="$CREDENTIALS_PASSPHRASE" \
--output _subscription_process/token.pickle _subscription_process/encrypted-token.pickle.gpg