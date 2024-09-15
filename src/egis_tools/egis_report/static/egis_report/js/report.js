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
    var field_amount = urlToJson(window.location.href)["amount"]
    var last_elem = null;
    for (i = 0; i < field_amount; i++)
    {
        let elem = document.createElement("div")
        elem.setAttribute("class", "file_upload_field")
        let label = document.createElement("label")
        label.setAttribute("class", "file_amount_input_label")
        label.setAttribute("for", 'xlsx_file_' + i)
        label.innerHTML = 'Link #' + (i + 1)

        let input = document.createElement("input")
        input.setAttribute("class", "url_input_field")
        input.setAttribute("type", "text")
        input.required = true;
        input.setAttribute("name", "xlsx_file_" + i)
        let select = document.createElement("select")
        select.setAttribute("class", "file_upload_select")
        select.innerHTML = '<option value="URL">URL</option><option value="File">File</option>'
        // adding event listener to change field when select value changes

        elem.appendChild(label)
        elem.appendChild(input)
        elem.appendChild(select)

        first_file_upload_field = document.getElementById("first_file_upload_field");
        form.insertBefore(elem, first_file_upload_field);
    }
}


function changeListener(event)
{
    var target_elem = event.target
    if (target_elem.nodeName == "SELECT")
    {
        console.log("its select" + target_elem)
        if (target_elem.value == "File")
        {
            var url_input_field = target_elem.parentNode.getElementsByClassName("url_input_field")[0]
            url_input_field.setAttribute("type", "file")
        }
        else if (target_elem.value == "URL")
        {
            var url_input_field = target_elem.parentNode.getElementsByClassName("url_input_field")[0]
            url_input_field.setAttribute("type", "text")
        }
        else
        {
            throw "Incorrect select value"
        }
    }
}

addEventListener("change", changeListener)


















