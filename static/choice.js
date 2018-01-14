$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-choice .modal-content").html("");
        $("#modal-choice").modal("show");
      },
      success: function (data) {
        $("#modal-choice .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#choice-table tbody").html(data.html_choice_list);
          $("#modal-choice").modal("hide");
        }
        else {
          $("#modal-choice .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-choice").click(loadForm);
  $("#modal-choice").on("submit", ".js-choice-create-form", saveForm);

  // Update book
  $("#choice-table").on("click", ".js-update-choice", loadForm);
  $("#modal-choice").on("submit", ".js-choice-update-form", saveForm);

  // Delete book
  $("#choice-table").on("click", ".js-delete-choice", loadForm);
  $("#modal-choice").on("submit", ".js-choice-delete-form", saveForm);

});
