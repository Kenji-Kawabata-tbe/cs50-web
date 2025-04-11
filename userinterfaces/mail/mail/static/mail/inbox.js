document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  // inpbox.html#emails-viewを非表示
  document.querySelector('#emails-view').style.display = 'none';
  // inpbox.html#compose-viewを表示
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  // TO、Subject、Bodyを空にする
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  // 選択されたメールボックスの名前を1文字目は大文字にしてh3タグで表示する。
  //  引数がinboxの場合、Inboxになる。
  //    mailbox.charAt(0).toUpperCase() は最初の1文字（"i"）を大文字（"I"）に
  //    mailbox.slice(1)  2文字目以降（"nbox"）を取り出す
  //
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}
