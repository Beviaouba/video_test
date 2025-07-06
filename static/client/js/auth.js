document.getElementById('regist-submit').addEventListener('click', function () {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var url = this.getAttribute('data-url');
    var csrfToken = document.getElementById('django-csrf-token').value;

    if (!username || !password) {
        alert('缺少必要字段');
        return;
    }

    var formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('csrfmiddlewaretoken', csrfToken);

    fetch(url, {
        method: 'POST',
        body: formData,
        credentials: 'same-origin'
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        alert(data.msg);
    })
    .catch(function (e) {
        console.log('error:%s', e);
    });
});


document.getElementById('login-submit').addEventListener('click', function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var url = this.getAttribute('data-url');
    var csrfToken = document.getElementById('django-csrf-token').value;

    if (!username || !password) {
        alert('缺少必要字段');
        return;
    }

    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 400) {
            try {
                var data = JSON.parse(xhr.responseText);
                if (data.code) {
                    alert(data.msg);
                } else {
                    window.location.href = 'client/video/ex';
                }
            } catch (e) {
                console.error('解析响应失败:', e);
                alert('服务器响应格式错误');
            }
        } else {
            console.error('请求失败:', xhr.statusText);
            alert('请求失败: ' + xhr.statusText);
        }
    };

    xhr.onerror = function() {
        console.error('网络请求失败');
        alert('网络请求失败，请检查连接');
    };

    var formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('csrfmiddlewaretoken', csrfToken);

    xhr.send(formData);
});

