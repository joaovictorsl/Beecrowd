#include <iostream>
#include <vector>

using namespace std;

int josephus(vector<int> &, int, int = 0, int = 0);

int main()
{
  int cases{}, people{}, step{}, answ{};
  cin >> cases;
  for (size_t i = 1; i <= cases; i++)
  {
    cin >> people >> step;
    vector<int> people_vector{};
    for (size_t i = 1; i <= people; i++)
    {
      people_vector.push_back(i);
    }

    answ = josephus(people_vector, step);

    cout << "Case " << i << ": " << answ << endl;
  }

  return 0;
}

int josephus(vector<int> &people_vector, int default_step, int step, int stopped_at)
{
  if (people_vector.size() == 1)
  {
    return people_vector.at(0);
  }
  int index_limit = people_vector.size() - 1;
  int index_to_erase{};
  if (step > 0)
  {
    index_to_erase = step + stopped_at - 1;
    if (index_to_erase == index_limit)
    {
      people_vector.pop_back();
      return josephus(people_vector, default_step);
    }
    else if (index_to_erase > index_limit)
    {
      step = step - (index_limit - stopped_at) - 1;
      return josephus(people_vector, default_step, step);
    }
    else
    {
      people_vector.erase(people_vector.begin() + index_to_erase);
      stopped_at = index_to_erase;
      step = 0;
      return josephus(people_vector, default_step, step, stopped_at);
    }
  }
  else
  {
    index_to_erase = default_step + stopped_at - 1;
    if (index_to_erase == index_limit)
    {
      people_vector.pop_back();
      return josephus(people_vector, default_step);
    }
    else if (index_to_erase > index_limit)
    {
      step = default_step - (index_limit - stopped_at) - 1;
      return josephus(people_vector, default_step, step);
    }
    else
    {
      people_vector.erase(people_vector.begin() + index_to_erase);
      stopped_at = index_to_erase;
      return josephus(people_vector, default_step, step, stopped_at);
    }
  }
}