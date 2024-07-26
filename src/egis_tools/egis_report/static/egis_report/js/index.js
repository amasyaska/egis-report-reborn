function insert_file_inputs()
{
    let field_amount = document.getElementById("xlsx_files_amount").value
    document.body.removeChild(document.getElementById("content_vertical_center"))
    let file_upload_form_wrapper = document.createElement("div")
    file_upload_form_wrapper.setAttribute("id", "file_upload_form_wrapper")
    let loader = document.createElement("div")
    loader.setAttribute("class", "loader")
    loader.setAttribute("id", "loader")
    let form = document.createElement("form")
    form.setAttribute("id", "file_upload_form")
    form.method = "POST"

    for (i = 0; i < field_amount; i++)
    {
        let elem = document.createElement("div")
        elem.innerHTML = '<label class="file_amount_input_label" for="xlsx_file_' + i + '">Enter link #' + (i + 1) + ': </label>'
        elem.innerHTML += '<input class="url_input_field" type="text" name="xlsx_file_' + i + '">'
        form.appendChild(elem)
        form.appendChild(document.createElement("br"))
    }
    let project_name_div = document.createElement("div")
    project_name_div.innerHTML = '<label class="file_amount_input_label" for="project_name">Enter project name: </label>'
    project_name_div.innerHTML += '<input class="url_input_field" type="text" name="project_name">'
    form.appendChild(project_name_div)
    form.appendChild(document.createElement("br"))

    let project_pseudonyms_div = document.createElement("div")
    project_pseudonyms_div.innerHTML = '<label class="file_amount_input_label" for="project_pseudonyms">Enter project pseudonyms separated by comma: </label>'
    project_pseudonyms_div.innerHTML += '<input class="url_input_field" type="text" name="project_pseudonyms">'
    form.appendChild(project_pseudonyms_div)

    let hidden_field = document.createElement("input") // input to send files amount through form
    hidden_field.setAttribute("name","xlsx_files_amount")
    hidden_field.setAttribute("type","hidden")
    hidden_field.setAttribute("value", field_amount)
    form.appendChild(hidden_field)

    let button_get_report = document.createElement("input")
    button_get_report.type = "submit"
    button_get_report.value = "Get report!"
    button_get_report.setAttribute("onclick", "show_loader_form()")
    button_get_report.setAttribute("class", "next_button")
    form.appendChild(document.createElement("br"))
    form.appendChild(document.createElement("br"))
    form.appendChild(button_get_report)

//    document.body.appendChild(loader)
//    hide_loader_form()
    file_upload_form_wrapper.appendChild(form)
    document.body.appendChild(file_upload_form_wrapper)
}

function show_loader_form() {
    document.getElementById("file_upload_form").style.display = "none"
    document.getElementById("loader").style.display = "block"
}

function hide_loader_form() {
    document.getElementById("file_upload_form").style.display = "block"
    document.getElementById("loader").style.display = "none"
}

window.addEventListener("load", hide_loader_form)
