function urlToJson(url)
{
    var regex = /[?&]([^=#]+)=([^&#]*)/g;
    var params = {};
    var match;

    while (match = regex.exec(url))
    {
        params[match[1]] = match[2];
    }

    return params;
}
