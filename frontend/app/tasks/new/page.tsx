import Link from "next/link";
import TaskForm from "../../_components/TaskForm";
import { getMe } from "../../_lib/server";

export default async function TaskCreatePage() {
  const me = await getMe(); // 未ログインならログイン画面へ

  return (
    <>
      <h1>ToDo Create!!!</h1>
      <Link href="/">タスク一覧へ戻る</Link>
      <p>
        <b>Current User is {me.username}</b>
      </p>
      <TaskForm />
    </>
  );
}
