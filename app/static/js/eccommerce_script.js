
$(document).ready(function(){
    renderEccommerce();
})

function renderEccommerce(){
    $.get(utils.routes.eccommerce, function(data, status){
        if (status == 'success'){
            utils.cl(data);
            var categoryHtmlOptions = '';
            var brandHtmlOptions = '';
            var contentHtml = '';
            var contentHtmlCards = '';

            for (var x = 0; x < data.length; x++){

                if (categoryHtmlOptions.indexOf(`<option value="${data[x].category}">${data[x].category}</option>`) === -1) categoryHtmlOptions += `<option value="${data[x].category}">${data[x].category}</option>`;
                if (brandHtmlOptions.indexOf(`<option value="${data[x].brand}">${data[x].brand}</option>`) === -1) brandHtmlOptions += `<option value="${data[x].brand}">${data[x].brand}</option>`;

                contentHtmlCards += `<div class="col-sm-12 col-lg-3 my-2">
                                        <div class="card shadow">
                                            <img class="card-img-top" src="${data[x].item.img_src}" alt="Card image" height="300px">
                                            <div class="card-body">
                                                <h6 class="card-title">${data[x].title.substring(0, 50)} ${data[x].title.length > 50 ? '...' : data[x].title.length < 31 ? '<p class="mb-0">&nbsp;</p>' : '...'}</h4>
                                                <p class="card-text">Some example text.</p>
                                                <a href="/eccommerce/${data[x].id}" class="btn btn-primary">See Profile</a>
                                            </div>
                                        </div>
                                    </div>`
            }

            formselectorsHTML = `
                <div class="row my-3">
                    <div class="col">
                        <label class="form-label">Category</label>
                        <select class="form-select" id= "category_selector" onchange="category_selector_fxn()">
                            <option value="all" selected>All</option>
                            ${categoryHtmlOptions}
                        </select>
                    </div>
                    <div class="col">
                        <label class="form-label">Brands</label>
                        <select class="form-select" id="brand_selector">
                            <option value="all" selected>All</option>
                            ${brandHtmlOptions}
                        </select>
                    </div>
                </div>`

            contentHtml = `
                <div class="row">
                    ${contentHtmlCards}
                </div>`;

            $('#form_selectors').html(formselectorsHTML);
            $('#content').html(contentHtml);

        }else{
            $('#content').html(`
                    <div>
                        <p class="fw-bold text-danger">No Items Found...</p>
                    </div>
                `);
        }
      });
    
}


function rendercontentHtmlCards(data){
    var contentHtmlCards = '';
    var brandHtmlOptions = '';
    for (var x = 0; x < data.length; x++){
        if (brandHtmlOptions.indexOf(`<option value="${data[x].brand}">${data[x].brand}</option>`) === -1) brandHtmlOptions += `<option value="${data[x].brand}">${data[x].brand}</option>`;
        contentHtmlCards += `<div class="col-sm-12 col-lg-3 my-2">
                                <div class="card shadow">
                                    <img class="card-img-top" src="${data[x].item.img_src}" alt="Card image" height="300px">
                                    <div class="card-body">
                                        <h6 class="card-title">${data[x].title.substring(0, 50)} ${data[x].title.length > 50 ? '...' : data[x].title.length < 31 ? '<p class="mb-0">&nbsp;</p>' : '...'}</h4>
                                        <p class="card-text">Some example text.</p>
                                        <a href="/eccommerce/${data[x].id}" class="btn btn-primary">See Profile</a>
                                    </div>
                                </div>
                            </div>`
    }
    return {contentHtmlCards, brandHtmlOptions}
}


function category_selector_fxn(){
    console.log( $('#category_selector').val() );
    var searchParam = $('#category_selector').val();
    
    $.get(`${searchParam === "all" ? utils.routes.eccommerce : utils.routes.eccommerceCategory + searchParam + "/"}`, function(data, status){
        if (status == 'success'){
            var {contentHtmlCards, brandHtmlOptions} = rendercontentHtmlCards(data);
            $('#content').html(`<div class="row">${contentHtmlCards}</div>`);
            $("#brand_selector").html(`<option value="all" selected>All</option>${brandHtmlOptions}</select>`)
        }else{
            $('#content').html("<h3>Error</h3>");
        }
    })
}

function renderMovies(){
    utils.cl('renderMovies')
}