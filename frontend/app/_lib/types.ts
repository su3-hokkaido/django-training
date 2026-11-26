export type Task = {
  id: number;
  title: string;
  description: string | null;
  completed: boolean;
};

export type User = {
  username: string;
};
