<h1> api_final_yatube </h1>

<h3> О проекте: </h3>
<p> API_FINAL_YATUBE - API для сервиса YATUBE </p>

<p> API доступен только аутентифицированным пользователям.
Авторизация реализована через JWT+Djoser.
Аутентифицированный пользователь авторизован на изменение и удаление своего контента - постов и комментариев;
в остальных случаях доступ предоставляется только для чтения.
Авторизованный пользователь так же имеет возможность
частичного редактирования и удаления контента, а также возможность подписаться на других пользователей.
</p>

<h3> Эндпоинты API: </h3>
<p>
<li> api/v1/jwt/create/ (POST): передаём логин и пароль, получаем токен. </li>
<li> api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост. </li>
<li> api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором{post_id}. </li>
<li> api/v1/groups/ (GET): получаем список всех групп. </li>
<li> api/v1/groups/{group_id}/ (GET): получаем информацию о группе с идентификатором {group_id}. </li>
<li> api/v1/posts/{post_id}/comments/ <br>
(GET): получаем список всех комментариев поста с идентификатором post_id <br>
(POST): создаём новый комментарий для поста с идентификатором {post_id}. </li>
<li> api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий с идентификатором {comment_id} в посте с id=post_id. </li>
<li> api/v1/follow/ (POST): создаем пару user - following </li>
</p>
<p> Для запуска проекта: </p>
<code>
git clone https://github.com/Addener/api_final_yatube.git
</code>
<code>
python -m venv venv
</code>
<code>
python -m pip install --upgrade pip
</code>
<code>
pip install -r requirements.txt
</code>
<p> Выполняем migrate: </p>
<code>
cd yatube_api
</code>
<code>
python manage.py migrate
</code>
<p> Запустите проект: </p>
<code>
python manage.py runserver
</code>


<p> <h3> Автор </h3> 
Ужва Алексей
</p>