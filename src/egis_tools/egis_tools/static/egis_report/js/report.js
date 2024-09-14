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

window.onload = function ()
{
    var form = document.getElementById("file_upload_form")
    var field_amount = urlToJson(window.location.href)
    for (i = 0; i < field_amount; i++)
    {
        let elem = document.createElement("div")
        elem.setAttribute("class", "file_upload_field")
        let label = document.createElement("label")
        label.setAttribute("class", "file_amount_input_label")
        label.setAttribute("for", 'xlsx_file_' + i)
        label.innerHTML = 'Link #' + (i + 1)

        let input = document.createElement("input")
        input.setAttribute("class", "file_upload_url")
        input.setAttribute("type", "text")
        input.setAttribute("name", "xlsx_file_" + i)
        let select = document.createElement("select")
        select.setAttribute("class", "file_upload_select")
        select.innerHTML = '<option value="URL">URL</option><option value="File">File</option>'
        // adding event listener to change field when select value changes
        select.addEventListener("change", change_file_upload_field)

        elem.appendChild(label)
        elem.appendChild(input)
        elem.appendChild(select)

        form.appendChild(elem)
        form.appendChild(document.createElement("br"))
    }
}
