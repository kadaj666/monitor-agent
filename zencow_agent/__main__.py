#!/usr/bin/env python3

import connexion

from zencow_agent import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'DevOpsHelper'})
    app.run(port=9000)


if __name__ == '__main__':
    main()
