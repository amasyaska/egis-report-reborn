function insert_file_inputs()
{
    let field_amount = document.getElementById("xlsx_files_amount").value
    document.body.innerHTML = ""
    let form = document.createElement("form")
    form.method = "POST"

    for (i = 0; i < field_amount; i++)
    {
        let elem = document.createElement("div")
        elem.innerHTML = '<label class="file_amount_input_label" for="xlsx_file_' + i + '">Enter link: </label>'
        elem.innerHTML += '<input class="url_input_field" type="text" name="xlsx_file_' + i + '">'
        form.appendChild(elem)
        form.appendChild(document.createElement("br"))
    }
    
    let hidden_field = document.createElement("input") // input to send files amount through form
    hidden_field.setAttribute("name","xlsx_files_amount")
    hidden_field.setAttribute("type","hidden")
    hidden_field.setAttribute("value", field_amount)
    form.appendChild(hidden_field)

    let button_get_report = document.createElement("input")
    button_get_report.type = "submit"
    button_get_report.value = "Get report!"
    form.appendChild(button_get_report)

    document.body.appendChild(form)
}
