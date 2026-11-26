import Link from "next/link";
import AuthForm from "../_components/AuthForm";

export default function LoginPage() {
  return (
    <>
      <h1>ToDo Login</h1>
      <AuthForm
        action="/api/auth/login/"
        fields={[
          { name: "username", label: "ユーザー名", type: "text", autoComplete: "username" },
          { name: "password", label: "パスワード", type: "password", autoComplete: "current-password" },
        ]}
        submitLabel="Login"
      />
      <p>You have no account?</p>
      <Link href="/register/">Create New User</Link>
    </>
  );
}
