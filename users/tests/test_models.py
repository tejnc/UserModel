from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):
    
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username")
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', first_name='firstname1', password="password1", is_superuser=False
            )
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', first_name='firstname1', password='password1', is_staff=False
            )
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='username1', first_name='firstname1', password='password1', is_staff=False
            )