var should = require('chai').should(),
    assert = require('better-assert'),
    parser = require('../');

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

    it('should return undefined on failure', function () {
      var url = 'git://github.com/justgord/.git';
      parser(url).should.equal('github.com/justgord/.git');
    });

    it('should parse git@gist urls', function () {
      var url = 'git@gist.github.com:3135914.git';
      parser(url).should.equal('gist.github.com/3135914.git');
    });

    it('should parse https://gist urls', function () {
      var url = 'https://gist.github.com/3135914.git';
      parser(url).should.equal('gist.github.com/3135914.git');
    });

    it('should parse git@github urls', function () {
      var url = 'git@github.com:AdoHe/ImageServer.git';
      parser(url).should.equal('github.com/AdoHe/ImageServer.git');
    });

    it('should parse company specific git@* urls', function () {
      var url = 'git@dev.sh.westudio.com:framework/Tunnel.git';
      parser(url).should.equal('dev.sh.westudio.com/framework/Tunnel.git');
    });

    it('should abc', function () {
      var url = 'ssh://user@host.xz:1234/path/to/repo.git';
      parser(url).should.equal('host.xz:1234/path/to/repo.git');
    });
    it('should abc2', function () {
      var url = 'https://user:passwd@host.xz:1234/path/to/repo.git';
      parser(url).should.equal('host.xz:1234/path/to/repo.git');
    });
    it('should abc3', function () {
      var url = 'user@host.xz:~user/path/to/repo.git';
      parser(url).should.equal('host.xz/~user/path/to/repo.git');
    });
    it('should abc4', function () {
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
})
