$(document).ready(function () {
  // Handle click event on translate button
  $('#btn_translate').click(function () {
    // Get language code from input field
    const languageCode = $('#language_code').val();

    // Fetch translation from API
    $.get('https://fourtonfish.com/hellosalut/?lang=' + languageCode, function (data) {
      // Display translation in hello div
      $('#hello').text(data.hello);
    });
  });
});
