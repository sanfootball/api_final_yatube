from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['following']
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='user_following_unique')
        ]

    def __str__(self):
        return self.user
