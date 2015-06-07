function likeHandler() {
    var articleDiv = $(this).parent();
    var articleId = articleDiv.attr('id');
    $.ajax({
        url: '/articles/' + articleId + '/addlike/', // articles/3/addlike/
        data: null
    }).done(function(data) {
        articleDiv.find('.likes').text(data.count);
    }).fail(function(){
        alert('Failed!');
    });
}

$('.like').on('click', likeHandler);

