var re = /^(([\w]+):\/\/)?((.+)(:(.+))?@)?(((([\w\d]+)(\.[\w\d]+)+)(:([\d]+))?)(?=[:\/]))?(([:\/])?((([^\/]+\/)+)?([^\/]+(\.git)?)))\/?$/

module.exports = urlFromGit;

function urlFromGit (url) {
    try {
        var m = re.exec(url);
        if (!m) return undefined
        var protocol = m[2] ? m[2]:"";
        var user = m[4] ? m[4]:"";
        var pass = m[6] ? m[6]:"";
        var fqdn_port = m[8] ? m[8]+'/':"";
        var fqdn = m[9] ? m[9]:"";
        var port = m[13] ? m[13]:"";
        var path = m[16];
        var namespace = m[17] ? m[17].trimEnd('/'):"";
        var project = m[19] ? m[19]:"";
        return fqdn_port + path;
    } catch (err) {
        // ignore
    }
};

urlFromGit.re = re;
