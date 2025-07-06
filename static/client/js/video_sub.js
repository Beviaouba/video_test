

document.getElementById('comment-submit').addEventListener('click', function() {
  // 获取元素和属性值
  var contentInput = document.getElementById('comment-content');
  var csrfToken = document.getElementById('django-csrf-token').value;
  var content = contentInput ? contentInput.value : null;
  var videoId = this.getAttribute('data-video-id');
  var userId = this.getAttribute('data-user-id');
  var url = this.getAttribute('data-url');

  // 内容校验
  if (!content) {
    alert('你还没有评论！');
    return;
  }
  console.log(url)

  // 创建表单数据
  var formData = new FormData();
  formData.append('content', content);
  formData.append('videoId', videoId);
  formData.append('userId', userId);
  formData.append('csrfmiddlewaretoken', csrfToken);

  // 发送 AJAX 请求
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url, true);

  xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 400) {
      console.log(xhr.responseText);
    } else {
      console.error('请求失败: ' + xhr.status);
    }
  };

  xhr.onerror = function() {
    console.error('请求出错');
  };

  xhr.send(formData);
});
