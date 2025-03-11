// ローカルストレージの値をチェック
if (!localStorage.getItem('counter')) {
    localStorage.getItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    //ローカルストレージのcounterを更新
    localStorage.setItem('counter', counter);

    //if (counter % 10 === 0) {
    //    alert(`Count is now ${counter}`);
    //}
}

document.addEventListener('DOMContentLoaded', function() {
    //最初からh1の値をローカルストレージのcounterの値にする
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;

    //setInterval(count, 1000);
});
