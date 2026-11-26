import Link from "next/link";
import AuthForm from "../_components/AuthForm";

export default function RegisterPage() {
  return (
    <>
      <h1>Create New User!!</h1>
      <AuthForm
        action="/api/auth/register/"
        fields={[
          { name: "username", label: "ユーザー名", type: "text", autoComplete: "username" },
          { name: "password1", label: "パスワード", type: "password", autoComplete: "new-password" },
          { name: "password2", label: "パスワード(確認用)", type: "password", autoComplete: "new-password" },
        ]}
        submitLabel="Create"
      />
      <p>You already have your account?</p>
      <Link href="/login/">Back to Login page</Link>
    </>
  );
}
