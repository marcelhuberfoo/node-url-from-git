import re
from pathlib import Path

CONDENSED_FILENAME = Path(__file__).parent.joinpath('regex_generated.asc')


# From here: https://stackoverflow.com/a/14919203
def unverbosify_regex_simple(verbose_re):
    WS_RX = r'(?<!\\)((\\{2})*)\s+'
    CM_RX = r'(?m)(?<!\\)((\\{2})*)#.*$'

    return re.sub(WS_RX, "\\1", re.sub(CM_RX, "\\1", verbose_re))


def unverbosify_regex_javascript(verbose_re):
    GROUPNAME_RX = r'\?P<\w+>'
    SLASH_RX = r'/'
    FLAGS_RX = r'\(\?[aiLmsux]+\)'

    intermediate_re = unverbosify_regex_simple(verbose_re)
    return '/' + re.sub(FLAGS_RX, "", re.sub(SLASH_RX, "\\/", re.sub(GROUPNAME_RX, "", intermediate_re))) + '/'


urls = [
    # tag::test-urls[]
    'ssh://user@host.xz:1234/path/to/repo.git/',
    'ssh://user@host.xz/path/to/repo.git/',
    'ssh://host.xz:1234/path/to/repo.git/',
    'ssh://host.xz/path/to/repo.git/',
    'ssh://user@host.xz/path/to/repo.git/',
    'ssh://host.xz/path/to/repo.git/',
    'ssh://user@host.xz/~user/path/to/repo.git/',
    'ssh://host.xz/~user/path/to/repo.git/',
    'ssh://user@host.xz/~/path/to/repo.git',
    'ssh://host.xz/~/path/to/repo.git',
    'user@host.xz:/path/to/repo.git/',
    'host.xz:/path/to/repo.git/',
    'user@host.xz:~user/path/to/repo.git/',
    'host.xz:~user/path/to/repo.git/',
    'user@host.xz:path/to/repo.git',
    'host.xz:path/to/repo.git',
    'rsync://host.xz/path/to/repo.git/',
    'git://host.xz/path/to/repo.git/',
    'git://host.xz/~user/path/to/repo.git/',
    'http://host.xz/path/to/repo.git/',
    'https://host.xz/path/to/repo.git/',
    'https://user@host.xz/path/to/repo.git/',
    'https://user:passwd@host.xz/path/to/repo.git/',
    'https://user:passwd@host.xz:1234/path/to/repo.git/',
    '/path/to/repo.git/',
    'path/to/repo.git/',
    '~/path/to/repo.git',
    'file:///path/to/repo.git/',
    'file://~/path/to/repo.git/',
    'repo.git',
    './path:repo.git',
    'git://github.com/justgord/.git',
    'git@github.com:marcelhuberfoo/node-url-from-git.git'
    # end::test-urls[]
]
# THIS IS THE MASTER RE!
GIT_URL_RX = re.compile(r"""(?m)                        # match multi line string
^                           # match from the beginning of the line
  (?P<scheme>               # 1:  (optional) scheme section, missing implicitly means `ssh://`
    (?P<protocol>[\w]+)     # 2:  access protocol
    ://
  )?
  (?P<credentials>          # 3:  (optional) credentials
    (?P<user>[^:]+)         # 4:  user to authenticate with
    (:                      # 5:  (optional) password section
      (?P<pass>[^@]+)       # 6:  password
    )?
    @
  )?
  (                         # 7:  (optional) FQDN section if : or / follows
    (?P<fqdn>               # 8:  FQDN including port
      (?P<host>             # 9:  name part of fqdn, requires at least a two part name
        ([\w\d]+            # 10: hostname
          (\.[\w\d]+)+      # 11: domainname
        )
      )
      (:                    # 12: (optional) port section
        (?P<port>[\d]+)     # 13: port number
      )?
    )
    (?=[:/])                # 14: lookahead assertion; only match previous group if : or / matches next
  )?
  (?P<scporpath>[:/])?      # 15: (optional) separator between fqdn and path section
  (?P<pathtorepo>           # 16: path/namespace and repository name
    (                       # 17: (optional) namespace section if / follows
      (?P<namespace>        # 18: path/namespace
        ([^/]+              # 19: first path segment
          (/[^/]+)*         # 20: any further path segment
        )
      )
      (?=[/])               # 21: lookahead assertion; only match previous group if / matches next
    )?
    /?
    (?P<project>[^/]+       # 22: repository name with optional .git suffix
      (\.git)?              # 23: (optional) .git suffix
    )
  )
  /?                        # according to git url examples, a terminating slash might be part of the url
$                           # until the end of the line
""", re.X)
for u in urls:
    print("URL [{0}]\n{1}".format(u, GIT_URL_RX.search(u).groupdict()))

condensed_re_py = unverbosify_regex_simple(GIT_URL_RX.pattern)
condensed_re_js = unverbosify_regex_javascript(GIT_URL_RX.pattern)

with open(CONDENSED_FILENAME, 'w') as f:
    f.write('tag::{tagname}[]\n{regex}\nend::{tagname}[]\n'.format(tagname='python-regex-verbose',
                                                                   regex=GIT_URL_RX.pattern))
    f.write('tag::{tagname}[]\n{regex}\nend::{tagname}[]\n'.format(tagname='python-regex', regex=condensed_re_py))
    f.write('tag::{tagname}[]\n{regex}\nend::{tagname}[]\n'.format(tagname='javascript-regex', regex=condensed_re_js))

# with open(CONDENSED_FILENAME, 'r') as f:
#     print(f.read())
