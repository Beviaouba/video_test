let videoAreaStatic = false;
const videoEditArea=document.getElementById('video-edit-area');


document.getElementById('open-add-video-btn').addEventListener('click', function() {
    if(!videoAreaStatic){
        videoEditArea.style.display = 'block';
        videoAreaStatic=true;
    }else {
        videoEditArea.style.display = 'none';
        videoAreaStatic=false;
    }
});