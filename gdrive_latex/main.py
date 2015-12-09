#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This package is part of the gdrive_latex package.
# Copyright © 2015 Evan W. Patton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

"""

import httplib2
import argparse
import logging

from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage
from os import environ
from sys import stderr


def download_file(filename, drive, http, parent_dir=None, alt_name=None):
    alt_name = alt_name or filename
    query = 'title contains "%s" and trashed=false' % filename
    if parent_dir is not None:
        dir_list = drive.files().list(q='title="%s" and trashed=false' % parent_dir).execute()
        if len(dir_list['items']) > 0:
            print "Found directory", dir_list['items'][0]['title']
            query += ' and "%s" in parents' % dir_list['items'][0]['id']
    file_list = drive.files().list(q=query).execute()
    content = None
    for item in file_list['items']:
        if 'exportLinks' in item:
            (_, content) = http.request(item['exportLinks']['text/plain'])
            if content is not None:
                break
    if content is None:
        raise KeyError('No export link found for file matching the name "%s"' % filename)
    with open(alt_name, 'w') as f:
        f.write(content)
        logging.info("Retrieved '%s' as '%s'." % (filename, alt_name))


def main():
    logging.basicConfig(stream=stderr, level=logging.INFO)
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('file', nargs='+')
    flags = parser.parse_args()
    flow = client.flow_from_clientsecrets('%s/.gdrive_latex_secret.json' % environ['HOME'],
                                          scope='https://www.googleapis.com/auth/drive',
                                          redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    storage = Storage('%s/.gdrive_latex' % environ['HOME'])
    credentials = storage.get() or tools.run_flow(flow, storage, flags)
    http_auth = credentials.authorize(httplib2.Http())

    drive_service = discovery.build('drive', 'v2', http_auth)
    for filename in flags.file:
        download_file(filename, drive_service, http_auth,
                      parent_dir=environ['PROJECT_DIR'] if 'PROJECT_DIR' in environ else None)


if __name__ == '__main__':
    main()
