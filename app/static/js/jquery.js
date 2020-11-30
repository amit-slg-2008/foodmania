$(document).ready(function(){
    $(function(){
        $.ajax({
            url: '/api/listOfProducts',
            type: 'GET',
            success: function(response)
            {
                data = response.products;
                for(var i=0;i<data.length;i++){
                    if(data[i]['quantity']>=1000){
                        product_qunatity = data[i]['quantity']/1000;
                        product_unit = "kg";
                    }else{
                        product_qunatity = data[i]['quantity'];
                        product_unit = data[i]['unit'];
                    }
                
                    $(".productlist").append('<div class="col-sm-3">\
                        <div class="card" style="width: 18rem;">\
                            <h5 class="card-title text-center">'+ data[i]['code'] + '-' + product_qunatity + product_unit +'</h5>\
                            <img src="/static/images/'+ data[i]['image'] + '" class="card-img-top cashewimage" alt="...">\
                            <div class="card-body">\
                                <span class="text-center">\
                                    <button type="button" class="fa fa-minus subtract" aria-hidden="true"></button>\
                                    <input class="quanbox" style="text-align: center;" type="text" value="1" min="1" readonly/>\
                                    <button type="button" class="fa fa-plus add" aria-hidden="true"></button>\
                                    <input type="hidden" class="hiddenquanbox" value="'+ data[i]['price'] +'" />\
                                </span>\
                                <p class="card-text text-center pricesection">Price : <span class="showprice">'+ data[i]['price'] +'</span></p>\
                                <button class="btn btn-success addtocart" data-id='+ data[i]['id'] +'>Add to Cart</button> \
                            </div>\
                        </div>\
                    </div>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });
        get_data_for_minicart();
        get_total_cart_items();
        get_data_for_cart();
        get_total_cart_value();
    });

    $(".searchsubmit").click(function(){
        var searchtext = $("#searchtext").val();
        $.ajax({
            url: '/api/searchProduct',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                'searchtext' : searchtext
            }),
            dataType: 'json',
            success: function(response)
            {
                data = response.products;
                $(".productlist").empty();
                for(var i=0;i<data.length;i++){
                    if(data[i]['quantity']>=1000){
                        product_qunatity = data[i]['quantity']/1000;
                        product_unit = "kg";
                    }else{
                        product_qunatity = data[i]['quantity'];
                        product_unit = data[i]['unit'];
                    }
                
                    $(".productlist").append('<div class="col-sm-3">\
                        <div class="card" style="width: 18rem;">\
                            <h5 class="card-title text-center">'+ data[i]['code'] + '-' + product_qunatity + product_unit +'</h5>\
                            <img src="/static/images/'+ data[i]['image'] + '" class="card-img-top cashewimage" alt="...">\
                            <div class="card-body">\
                                <span class="text-center">\
                                    <button type="button" class="fa fa-minus subtract" aria-hidden="true"></button>\
                                    <input class="quanbox" style="text-align: center;" type="text" value="1" min="1" readonly/>\
                                    <button type="button" class="fa fa-plus add" aria-hidden="true"></button>\
                                    <input type="hidden" class="hiddenquanbox" value="'+ data[i]['price'] +'" />\
                                </span>\
                                <p class="card-text text-center pricesection">Price : <span class="showprice">'+ data[i]['price'] +'</span></p>\
                                <button class="btn btn-success addtocart" data-id='+ data[i]['id'] +'>Add to Cart</button> \
                            </div>\
                        </div>\
                    </div>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });
    });

    $(document).on('click', '.add', function(){
        $quanbox = $(this).parent().find('.quanbox');
        $hiddenquanbox = $(this).parent().find('.hiddenquanbox');
        $showprice = $(this).parent().parent().find('.showprice');
        var newquan = parseInt($quanbox.val()) + 1;
        var newprice = parseInt($hiddenquanbox.val()) * newquan;
        $quanbox.val(newquan);
        $showprice.html(newprice);
    });

    $(document).on('click', '.subtract', function(){
        $quanbox = $(this).parent().find('.quanbox');
        $hiddenquanbox = $(this).parent().find('.hiddenquanbox');
        $showprice = $(this).parent().parent().find('.showprice');
        var newquan = parseInt($quanbox.val()) - 1;
        if(newquan >= 1){
            var newprice = parseInt($hiddenquanbox.val()) * newquan;
            $quanbox.val(newquan);
            $showprice.html(newprice);
        }
    });

    $(document).on('click','.addtocart',function(){
        var productid = $(this).attr('data-id');
        var quantity = $(this).parent().find('.quanbox').val();
        var price = $(this).parent().find('.hiddenquanbox').val();
        $.ajax({
            url: '/api/addToCart',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                'product' : productid,
                'quantity' : quantity,
                'price' : price
            }),
            dataType: 'json',
            success: function(response)
            {
                get_data_for_minicart();
                get_total_cart_items();
            }
        });
    });

    function get_total_cart_items(){
        $.ajax({
            url: '/api/totalItemsInCart',
            type: 'GET',
            success: function(response)
            {
                $('#totalitems').html(response.count);
            }
        });
    }

    function get_total_cart_value(){
        $.ajax({
            url: '/api/totalCartValue',
            type: 'GET',
            success: function(response)
            {
                $('#totalcartprice').html(response.total);
            }
        });
    }

    function get_data_for_minicart(){
        $.ajax({
            url: '/api/viewCartMini',
            type: 'GET',
            success: function(response)
            {
                data = response.cart;
                if(data === 'none'){
                    $('#minicartbody').empty();
                    $('#minicartbody').append('<tr>\
                        <td colspan="4" align="center">No items in cart to display</td> \
                    </tr>');
                }else{
                    $('#minicartbody').empty();
                    for(var i=0;i<data.length;i++){
                        if(data[i]['productquantity']>=1000){
                            product_qunatity = data[i]['productquantity']/1000;
                            product_unit = "kg";
                        }else{
                            product_qunatity = data[i]['productquantity'];
                            product_unit = data[i]['unit'];
                        }
                        $('#minicartbody').append('<tr>\
                            <td>'+ (i+1) +'</td> \
                            <td>'+ data[i]['productcode'] + '-' + product_qunatity + product_unit +'</td> \
                            <td>'+ data[i]['quantity'] + '</td> \
                            <td align="right">'+ data[i]['total'] + '</td> \
                        </tr>');
                    }
                    $('#minicartbody').append('<tr>\
                        <td colspan="3" align="center">Subtotal</td> \
                        <td align="right">'+ response.totalprice +'</td> \
                    </tr>');
                }
            }
        });
    }

    function get_data_for_cart(){
        $.ajax({
            url: '/api/viewCart',
            type: 'GET',
            success: function(response)
            {
                data = response.cart;
                datatotal = response.total;
                if(data === 'none'){
                    $('#cartbody').empty();
                    $('#cartbody').append('<tr>\
                        <td colspan="4" align="center">No items in cart to display</td> \
                    </tr>');
                }else{
                    $('#cartbody').empty();
                    for(var i=0;i<data.length;i++){
                        if(data[i]['productquantity']>=1000){
                            product_qunatity = data[i]['productquantity']/1000;
                            product_unit = "kg";
                        }else{
                            product_qunatity = data[i]['productquantity'];
                            product_unit = data[i]['unit'];
                        }
                        $('#cartbody').append('<tr>\
                            <td>'+ (i+1) +'</td> \
                            <td>'+ data[i]['productcode'] + '-' + product_qunatity + product_unit +'</td> \
                            <td>'+ data[i]['price'] + '</td> \
                            <td>\
                            <button type="button" class="fa fa-minus subtractproductcart" aria-hidden="true"></button>\
                            <input class="quanbox" type="text" style="text-align: center;" value="'+ data[i]['quantity'] +'" min="1" readonly/>\
                            <button type="button" class="fa fa-plus addproductcart" aria-hidden="true"></button>\
                            <input type="hidden" class="hiddenidbox" value="'+ data[i]['productid'] +'" />\
                            <input type="hidden" class="hiddenpricebox" value="'+ data[i]['price'] +'" /></td> \
                            <td align="right">'+ data[i]['total'] + '</td> \
                        </tr>');
                    }
                    $('#cartbody').append('<tr>\
                        <td colspan="4" align="right">Subtotal</td> \
                        <td align="right">'+ datatotal[0]['total'] +'</td> \
                    </tr><tr>\
                        <td colspan="4" align="right">CGST 9%</td> \
                        <td align="right">'+ datatotal[0]['cgst'] +'</td> \
                    </tr><tr>\
                        <td colspan="4" align="right">SGST 9%</td> \
                        <td align="right">'+ datatotal[0]['sgst'] +'</td> \
                    </tr><tr>\
                        <td colspan="4" align="right">Total</td> \
                        <td align="right">'+ datatotal[0]['grandtotal'] +'</td> \
                    </tr>');
                }
            }
        });
    }

    $(document).on('click', '.addproductcart', function(){
        $quanbox = $(this).parent().find('.quanbox');
        $hiddenidbox = $(this).parent().find('.hiddenidbox');
        $hiddenpricebox = $(this).parent().find('.hiddenpricebox');
        var newquan = parseInt($quanbox.val()) + 1;
        $quanbox.val(newquan);
        $.ajax({
            url: '/api/updateCartByProduct',
            type: 'PUT',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                'product' : $hiddenidbox.val(),
                'quantity' : $quanbox.val(),
                'price' : $hiddenpricebox.val()
            }),
            dataType: 'json',
            success: function(response)
            {
                
            },
            complete:function(){
                get_data_for_cart();
            }
        });
    });

    $(document).on('click', '.subtractproductcart', function(){
        $quanbox = $(this).parent().find('.quanbox');
        $hiddenidbox = $(this).parent().find('.hiddenidbox');
        $hiddenpricebox = $(this).parent().find('.hiddenpricebox');
        var newquan = parseInt($quanbox.val()) - 1;
        if(newquan >= 1){
            $quanbox.val(newquan);
            $.ajax({
                url: '/api/updateCartByProduct',
                type: 'PUT',
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({
                    'product' : $hiddenidbox.val(),
                    'quantity' : $quanbox.val(),
                    'price' : $hiddenpricebox.val()
                }),
                dataType: 'json',
                success: function(response)
                {
                    get_data_for_cart();
                }
            });
        }
    });

    $("#placeorder").click(function(){
        var name = $("#name").val();
        var email = $("#email").val();
        var contactno = $("#contactno").val();
        var address = $("#address").val();
        var creditcard = $("#creditcard").val();
        var ccmonth = $("#ccmonth").val();
        var ccyear = $("#ccyear").val();
        var cvv = $("#cvv").val();
        customerdata = {
            'name' : name,
            'email' : email,
            'contactno' : contactno,
            'address' : address,
            'creditcard' : creditcard,
            'ccmonth' : ccmonth,
            'ccyear' : ccyear,
            'cvv' : cvv
        }
        if(check(customerdata)==true){
            var userid;
            $.ajax({
                url: '/api/createCustomer',
                type: 'POST',
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(customerdata),
                dataType: 'json',
                success: function(response)
                {
                    userid = response.userid;
                },
                complete: function(){
                    place_order(userid);
                }
            });
        }
    });

    $("input").keypress(function(){
        $('.errormsg').html("");
    });

    function check(customerdata){
        var msg;
        if(customerdata['name']===""){
            msg = "*Name cannot be left blank";
            $errormsg = $("#name").parent().parent().find('.errormsg');
            $errormsg.html(msg);
            return false;
        }else if(customerdata['email']===""){
            msg = "*Email cannot be left blank";
            $errormsg = $("#email").parent().parent().find('.errormsg');
            $errormsg.html(msg);
            return false;
        }else if(customerdata['contactno']===""){
            msg = "*Contact No cannot be left blank";
            $errormsg = $("#contactno").parent().parent().find('.errormsg');
            $errormsg.html(msg);
            return false;
        }else if(customerdata['address']===""){
            msg = "*Address cannot be left blank";
            $errormsg = $("#address").parent().parent().find('.errormsg');
            $errormsg.html(msg);
            return false;
        }else if(customerdata['creditcard']===""){
            msg = "*Credit Card cannot be left blank";
            $errormsg = $("#creditcard").parent().find('.errormsg');
            $errormsg.html(msg);
            return false;
        }else if(customerdata['cvv']===""){
            msg = "*CVV cannot be left blank";
            $errormsg = $("#cvv").parent().find('.errormsg');
            $errormsg.html(msg);
            return false;
        }else{
            return true;
        }
    }

    function place_order(userid){
        console.log(userid);
        $.ajax({
            url: '/api/placeOrder',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                'userid' : userid
            }),
            dataType: 'json',
            success: function(response)
            {
                alert(response.message);
                window.location = "/";
            }
        });
    }

    $("#checkoutback").click(function(){
        window.location = "/viewcart";
    });

    $("#viewcartback").click(function(){
        window.location = "/";
    });

    $("#homecheckout").click(function(){
        window.location = "/viewcart";
    });

});