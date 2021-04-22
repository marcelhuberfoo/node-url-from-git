# node-url-from-git
![Build Status](https://travis-ci.com/marcelhuberfoo/node-url-from-git.svg?branch=master)

```js
describe('index.test.js', function () {

    it('should support git://*', function () {
      var url = 'git://github.com/jamesor/mongoose-versioner';
      parser(url).should.equal('github.com/jamesor/mongoose-versioner');
    });

    it('should support git://*.git', function () {
      var url = 'git://github.com/treygriffith/cellar.git';
      parser(url).should.equal('github.com/treygriffith/cellar.git');
    });

    it('should support https://*', function () {
      var url = 'https://github.com/Empeeric/i18n-node';
      parser(url).should.equal('github.com/Empeeric/i18n-node');
    });

    it('should parse https://*.git', function () {
      var url = 'https://jpillora@github.com/banchee/tranquil.git';
      parser(url).should.equal('github.com/banchee/tranquil.git');
    });

    it('should parse ssh url including port', function () {
      var url = 'ssh://user@host.xz:1234/path/to/repo.git';
      parser(url).should.equal('host.xz:1234/path/to/repo.git');
    });

    it('should parse https url including user:pass combination', function () {
      var url = 'https://user:passwd@host.xz:1234/path/to/repo.git';
      parser(url).should.equal('host.xz:1234/path/to/repo.git');
    });

    it('should parse short form ssh url with username', function () {
      var url = 'user@host.xz:~user/path/to/repo.git';
      parser(url).should.equal('host.xz/~user/path/to/repo.git');
    });

    it('should most simplistic local repo url', function () {
      var url = 'repo.git';
      parser(url).should.equal('repo.git');
    });
})

describe('re', function () {
    it('should get the url parse regex', function () {
        parser.re.source.should.equal(
          /^(([\w]+):\/\/)?((.+)(:(.+))?@)?(((([\w\d]+)(\.[\w\d]+)+)(:([\d]+))?)(?=[:\/]))?(([:\/])?((([^\/]+\/)+)?([^\/]+(\.git)?)))\/?$/.source
        )
    });
})```
