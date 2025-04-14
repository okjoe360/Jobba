var utils = {
    cl : (message) => {
        console.log({ message });
    },

    ce : (message)=>{
        console.error({ message });
    },

    getData : async ($url) => {
        var data, status;
        $.get($url, function(data, status){
            return data, status
          });
    },

    postData : async ($url, $formData) => {
        $.post($url, $formData, function(data, status){
            return data, status
        });
    },

    routes : {
                eccommerce: "/api/v1/store",
                eccommerceCategory: "/api/v1/store/category/",
                movies: "/api/v1/movies",
            }
}






